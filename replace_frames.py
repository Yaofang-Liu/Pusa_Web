import cv2
import os
import re
import glob
from tqdm import tqdm

def replace_last_frames():
    """
    Replaces the last four frames of MP4 videos in a directory with a specific image,
    attempting to use a web-compatible codec (H.264) first.
    """
    video_dir = "/home/dyvm6xra/dyvm6xrauser02/raphael/Pusa_Web/public/demos/outputs__multi_frames_dict_keys([0, 20])_30steps_0,0_copy"
    base_image_dir = "/home/dyvm6xra/dyvm6xrauser02/raphael/DiffSynth-Studio/video_text_pusa/frames"
    num_frames_to_replace = 4
    replacement_frame_name = "frame_000080.jpg"

    if not os.path.isdir(video_dir):
        print(f"Video directory not found: {video_dir}")
        return

    try:
        mp4_files = [f for f in os.listdir(video_dir) if f.lower().endswith('.mp4')]
        video_paths = sorted([os.path.join(video_dir, f) for f in mp4_files])
    except FileNotFoundError:
        print(f"Error accessing video directory: {video_dir}")
        return

    if not video_paths:
        print(f"No .mp4 files found in {video_dir}")
        return

    # --- Codec Selection Logic ---
    # We will try to use the best, most compatible codecs first.
    # 'avc1' or 'h264' are for H.264, the web standard.
    # 'mp4v' is the fallback that causes playback issues in browsers.
    preferred_codecs = ['avc1', 'h264']
    fallback_codec = 'mp4v'
    
    for video_path in tqdm(video_paths, desc="Processing videos"):
        filename = os.path.basename(video_path)
        
        match = re.search(r'MultiFrame_(\d+)_', filename)
        if not match:
            tqdm.write(f"Could not find identifier in {filename}. Skipping.")
            continue
        
        identifier = match.group(1)
        replacement_image_path = os.path.join(base_image_dir, identifier, replacement_frame_name)
        
        if not os.path.exists(replacement_image_path):
            tqdm.write(f"Replacement image not found at {replacement_image_path}. Skipping video {filename}.")
            continue

        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            tqdm.write(f"Error opening video file {video_path}. Skipping.")
            continue
        
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = cap.get(cv2.CAP_PROP_FPS)
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        replacement_frame = cv2.imread(replacement_image_path)
        if replacement_frame is None:
            tqdm.write(f"Error reading replacement image {replacement_image_path}. Skipping video {filename}.")
            cap.release()
            continue
        
        resized_replacement_frame = cv2.resize(replacement_frame, (width, height))
        
        temp_output_path = video_path + ".tmp.mp4"
        
        out = None
        used_codec = None

        # Try preferred codecs first
        for codec_str in preferred_codecs:
            fourcc = cv2.VideoWriter_fourcc(*codec_str)
            out = cv2.VideoWriter(temp_output_path, fourcc, fps, (width, height))
            if out.isOpened():
                used_codec = codec_str
                break
        
        # If preferred codecs failed, use the fallback
        if not out or not out.isOpened():
            fourcc = cv2.VideoWriter_fourcc(*fallback_codec)
            out = cv2.VideoWriter(temp_output_path, fourcc, fps, (width, height))
            used_codec = fallback_codec
            if out.isOpened():
                tqdm.write(f"Warning: Preferred codecs failed for {filename}. Using fallback '{fallback_codec}'.")
            else:
                 tqdm.write(f"FATAL: Could not open VideoWriter with any codec for {filename}.")
                 cap.release()
                 continue
        
        # tqdm.write(f"Processing {filename} with codec: {used_codec}")

        frames_to_keep = frame_count - num_frames_to_replace
        
        for i in range(frame_count):
            if i < frames_to_keep:
                ret, frame = cap.read()
                if not ret:
                    tqdm.write(f"Warning: Could not read frame {i} from {filename}. Stopping early.")
                    break
                out.write(frame)
            else:
                out.write(resized_replacement_frame)

        cap.release()
        out.release()
        
        os.replace(temp_output_path, video_path)

    print("\nProcessing complete.")

if __name__ == "__main__":
    replace_last_frames() 