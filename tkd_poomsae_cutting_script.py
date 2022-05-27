import os
import glob
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

########################################################################################################################

video_input_folder  = r'D:\OneDrive - inpe.br\TKD\0_taegeuk_poomsae'
output_folder = os.path.join(video_input_folder, r'output')
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

video_input_list    = glob.glob(os.path.join(video_input_folder, r'*.mp4'))
video_input_dict  = dict()

video_input_dict[video_input_list[0]] = {r'start_time': 81.5, r'end_time': 124}
video_input_dict[video_input_list[1]] = {r'start_time': 66.5, r'end_time': 111}
video_input_dict[video_input_list[2]] = {r'start_time': 69.5, r'end_time': 120}
video_input_dict[video_input_list[3]] = {r'start_time': 89.5, r'end_time': 141}
video_input_dict[video_input_list[4]] = {r'start_time': 72.5, r'end_time': 125}
video_input_dict[video_input_list[5]] = {r'start_time': 54.5, r'end_time': 113}
video_input_dict[video_input_list[6]] = {r'start_time': 60.5, r'end_time': 125}
video_input_dict[video_input_list[7]] = {r'start_time': 66.5, r'end_time': 136}

for input in video_input_list:
    output_path = os.path.join(output_folder, os.path.basename(input).replace(r'.mp4', r'_cut.mp4'))
    start_time = video_input_dict[input][r'start_time']
    end_time = video_input_dict[input][r'end_time']
    ffmpeg_extract_subclip(input, start_time, end_time, targetname=output_path)

########################################################################################################################

video_input_folder  = r'D:\OneDrive - inpe.br\TKD\0_taegeuk_yudanja'
output_folder = os.path.join(video_input_folder, r'output')
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

video_input_list    = glob.glob(os.path.join(video_input_folder, r'*.mp4'))
video_input_dict  = dict()

video_input_dict[video_input_list[0]] = {r'start_time': 48, r'end_time': 117}
video_input_dict[video_input_list[1]] = {r'start_time': 70.5, r'end_time': 177}
video_input_dict[video_input_list[2]] = {r'start_time': 51.5, r'end_time': 112}
video_input_dict[video_input_list[3]] = {r'start_time': 50, r'end_time': 116}
video_input_dict[video_input_list[4]] = {r'start_time': 54, r'end_time': 174}
video_input_dict[video_input_list[5]] = {r'start_time': 48.5, r'end_time': 133}
video_input_dict[video_input_list[6]] = {r'start_time': 52.5, r'end_time': 145}
video_input_dict[video_input_list[7]] = {r'start_time': 47.5, r'end_time': 113}
video_input_dict[video_input_list[8]] = {r'start_time': 48.5, r'end_time': 125}

for input in video_input_list:
    output_path = os.path.join(output_folder, os.path.basename(input).replace(r'.mp4', r'_cut.mp4'))
    start_time = video_input_dict[input][r'start_time']
    end_time = video_input_dict[input][r'end_time']
    ffmpeg_extract_subclip(input, start_time, end_time, targetname=output_path)


