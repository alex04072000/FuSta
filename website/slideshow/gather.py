import os

category = 'Selfie'
id = '30'

## for parallel (crop input)
# os.system('ffmpeg -i ../HTML/compressed_results/additional_comparisons/'+category+'/'+id+'_Input.mp4 -filter:v "crop=632:352" out.mp4')
# os.system('ffmpeg -i out.mp4 -i ../HTML/compressed_results/additional_comparisons/'+category+'/'+id+'_Ours.mp4 -filter_complex "[0]pad=iw+10:color=white[left];[left][1]hstack=inputs=2" '+category+'_'+id+'.mp4')

os.system('ffmpeg -i ../HTML/compressed_results/additional_comparisons/'+category+'/'+id+'_Input.mp4 -i ../HTML/compressed_results/additional_comparisons/'+category+'/'+id+'_Ours.mp4 -filter_complex "[0]pad=iw+10:color=white[left];[left][1]hstack=inputs=2" '+category+'_'+id+'.mp4')
