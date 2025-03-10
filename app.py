from flask import Flask, request, jsonify
import yt_dlp

app = Flask(__name__)

@app.route('/video-details', methods=['GET'])
def get_video_details():
    # Get the video URL from the query parameters
    video_url = request.args.get('url')

    # Check if the URL is provided
    if not video_url:
        return jsonify({"error": "No video URL provided"}), 400

    try:
        # Options for yt-dlp
        ydl_opts = {'quiet': True}
        
        # Use yt-dlp to extract video information without downloading
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=False)

        # Create a dictionary with relevant video details
        video_data = {
            "title": info_dict.get("title"),
            "uploader": info_dict.get("uploader"),
            "duration": info_dict.get("duration"),
            "thumbnail": info_dict.get("thumbnail"),
            "views": info_dict.get("view_count"),
            "like_count": info_dict.get("like_count"),
            "upload_date": info_dict.get("upload_date"),
            "direct_video_url": info_dict.get("url"),
        }

        # Return the video details as a JSON response
        return jsonify(video_data)

    except Exception as e:
        # Handle any errors and return a server error response
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Run the Flask application
    app.run(host="0.0.0.0", port=8080)
