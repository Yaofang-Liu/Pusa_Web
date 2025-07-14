import os
import sys

# This script is designed to be run from the root of your project directory
# (e.g., /home/dyvm6xra/dyvm6xrauser02/raphael).

# DRY_RUN = True  # Set to False to actually delete files. True will only list them.
DRY_RUN = False  # Set to False to actually delete files. True will only list them.

# --- Data extracted from Pusa_Web/src/pages/index.astro ---

VIDEO_DATA = [
    {
        "folder": "Pusa_Web/public/demos/outputs_I2V_first_frames_30steps_no_noise",
        "files_to_keep": [
            "MultiFrame_00015_epoch=5-step=900.ckpt_20250619_055745.mp4", "MultiFrame_00016_epoch=5-step=900.ckpt_20250619_032326.mp4",
            "MultiFrame_00046_epoch=5-step=900.ckpt_20250619_032554.mp4", "MultiFrame_00050_epoch=5-step=900.ckpt_20250619_060017.mp4",
            "MultiFrame_00053_epoch=5-step=900.ckpt_20250619_044332.mp4", "MultiFrame_00056_epoch=5-step=900.ckpt_20250619_032431.mp4",
            "MultiFrame_00007_epoch=5-step=900.ckpt_20250619_040022.mp4", "MultiFrame_00008_epoch=5-step=900.ckpt_20250619_043753.mp4",
            "MultiFrame_00063_epoch=5-step=900.ckpt_20250619_043938.mp4"
        ]
    },
    {
        "folder": "Pusa_Web/public/demos/outputs__multi_frames_dict_keys([0, 20])_30steps_0,0_rm_last_four_frames",
        "files_to_keep": [
            "MultiFrame_00007_epoch=5-step=900.ckpt_20250619_084250.mp4", "MultiFrame_00009_epoch=5-step=900.ckpt_20250619_095952.mp4",
            "MultiFrame_00016_epoch=5-step=900.ckpt_20250619_080832.mp4", "MultiFrame_00025_epoch=5-step=900.ckpt_20250619_103405.mp4",
            "MultiFrame_00027_epoch=5-step=900.ckpt_20250619_084549.mp4", "MultiFrame_00030_epoch=5-step=900.ckpt_20250619_104359.mp4",
        ]
    },
    {
        "folder": "Pusa_Web/public/demos/outputs__multi_frames_0,20_30steps_0.3,0.7_rm_last_four_frames",
        "files_to_keep": [
            'MultiFrame_00003_epoch=5-step=900.ckpt_20250618_233301.mp4', 'MultiFrame_00008_epoch=5-step=900.ckpt_20250618_231742.mp4',
            'MultiFrame_00031_epoch=5-step=900.ckpt_20250618_220752.mp4', 'MultiFrame_00048_epoch=5-step=900.ckpt_20250618_232521.mp4',
            'MultiFrame_00052_epoch=5-step=900.ckpt_20250618_224839.mp4', 'MultiFrame_00053_epoch=5-step=900.ckpt_20250618_232850.mp4',
        ]
    },
    {
        "folder": "Pusa_Web/public/demos/outputs_v2v_[0, 1, 2, 3]_30steps_0,0,0,0",
        "files_to_keep": [
            "V2V_00002_epoch=5-step=900.ckpt_20250620_093058.mp4", "V2V_00010_epoch=5-step=900.ckpt_20250620_141133.mp4",
            "V2V_00038_epoch=5-step=900.ckpt_20250620_093105.mp4", "V2V_00052_epoch=5-step=900.ckpt_20250620_120949.mp4",
            "V2V_00055_epoch=5-step=900.ckpt_20250620_084934.mp4", "V2V_00059_epoch=5-step=900.ckpt_20250620_112614.mp4",
        ]
    },
    {
        "folder": "Pusa_Web/public/demos/outputs_v2v_[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]_30steps_0,0,0,0,0,0,0,0,0,0,0",
        "files_to_keep": [
            "V2V_00038_epoch=5-step=900.ckpt_20250620_092820.mp4", "V2V_00042_epoch=5-step=900.ckpt_20250620_121118.mp4",
            "V2V_00045_epoch=5-step=900.ckpt_20250620_134555.mp4", "V2V_00064_epoch=5-step=900.ckpt_20250620_132843.mp4",
            "V2V_00066_epoch=5-step=900.ckpt_20250620_092535.mp4", "V2V_00068_epoch=5-step=900.ckpt_20250620_104734.mp4",
        ]
    },
    {
        "folder": "Pusa_Web/public/demos/outputs_Vbench_T2V_50_steps",
        "files_to_keep": [
            "A car changes from golden to white.-0.mp4", "A person is sitting in a chair, then they suddenly get up and start stretching.-2.mp4",
            "A rabbit with the horns of a goat, hopping energetically while butting through obstacles.-1.mp4",
            "A whale with the wings of a bat, soaring over the ocean surface under the full moon.-0.mp4",
            "A dog is on the left of a sofa, then the dog runs to the front of the sofa.-1.mp4", "A person is eating a hot dog.-1.mp4",
        ]
    },
    {
        "folder": "Pusa_Web/public/demos/outputs_v2v_[0, 20]_30steps_0,0",
        "files_to_keep": [
            'V2V_00011_epoch=5-step=900.ckpt_20250713_042431.mp4', 'V2V_00066_epoch=5-step=900.ckpt_20250713_120426.mp4',
            'V2V_00055_epoch=5-step=900.ckpt_20250713_045905.mp4', 'V2V_00004_epoch=5-step=900.ckpt_20250713_015310.mp4',
            'V2V_00061_epoch=5-step=900.ckpt_20250713_085318.mp4', 'V2V_00050_epoch=5-step=900.ckpt_20250713_014422.mp4',
            'V2V_00048_epoch=5-step=900.ckpt_20250713_121034.mp4', 'V2V_00009_epoch=5-step=900.ckpt_20250713_034114.mp4',
            'V2V_00034_epoch=5-step=900.ckpt_20250713_022429.mp4',
        ]
    },
    {
        "folder": "Pusa_Web/public/demos/outputs_v2v_[0, 1, 2, 18, 19, 20]_30steps_0,0,0,0,0,0",
        "files_to_keep": [
            'V2V_00049_epoch=5-step=900.ckpt_20250713_191620.mp4', 'V2V_00065_epoch=5-step=900.ckpt_20250714_001630.mp4',
            'V2V_00036_epoch=5-step=900.ckpt_20250713_035750.mp4', 'V2V_00067_epoch=5-step=900.ckpt_20250714_005919.mp4',
            'V2V_00014_epoch=5-step=900.ckpt_20250713_040101.mp4', 'V2V_00055_epoch=5-step=900.ckpt_20250713_212454.mp4',
        ]
    }
]


def clean_directories():
    """
    Iterates through the defined video directories and removes any files
    not present in the 'files_to_keep' lists.
    """
    if DRY_RUN:
        print("--- Running in DRY RUN mode. No files will be deleted. ---")
    else:
        print("--- WARNING: Running in LIVE mode. Files WILL be deleted. ---")
        
    base_path = os.getcwd()
    total_deleted = 0

    for item in VIDEO_DATA:
        directory = os.path.join(base_path, item["folder"])
        files_to_keep = set(item["files_to_keep"])

        print(f"\nProcessing directory: {directory}")

        if not os.path.isdir(directory):
            print(f"  -> Directory not found. Skipping.")
            continue

        dir_deleted_count = 0
        try:
            for filename in os.listdir(directory):
                if filename not in files_to_keep:
                    file_path = os.path.join(directory, filename)
                    if os.path.isfile(file_path):
                        action = "Would delete" if DRY_RUN else "Deleting"
                        print(f"  - {action}: {filename}")
                        if not DRY_RUN:
                            os.remove(file_path)
                        dir_deleted_count += 1
        except OSError as e:
            print(f"  -> ERROR accessing directory: {e}", file=sys.stderr)
            continue
        
        if dir_deleted_count == 0:
            print("  -> No files to remove from this directory.")
        else:
            total_deleted += dir_deleted_count
            summary = "would be deleted" if DRY_RUN else "were deleted"
            print(f"  -> Summary: {dir_deleted_count} files {summary}.")

    print("\n-----------------------------------------")
    print(f"Cleanup complete. Total files {('to be ' if DRY_RUN else '')}deleted: {total_deleted}")
    print("-----------------------------------------")


if __name__ == "__main__":
    clean_directories() 