# Change to the video id of the YouTube video
# video id is the last part of the url http://youtube.com/watch?v=video_id
VIDEO_ID = "2jdoYHib89s"

parser = argparse.ArgumentParser(
    description="Example on how to use the Youtube Controller."
)

parser.add_argument("--show-debug", help="Enable debug log", action="store_true")

parser.add_argument(
    "--cast", help='Name of cast device (default: "%(default)s")', default=CAST_NAME
)
parser.add_argument(
    "--videoid", help='Youtube video ID (default: "%(default)s")', default=VIDEO_ID
)
args = parser.parse_args()

if args.show_debug:
    logging.basicConfig(level=logging.DEBUG)

chromecasts = pychromecast.get_listed_chromecasts(friendly_names=[args.cast])
if not chromecasts:
    print('No chromecast with name "{}" discovered'.format(args.cast))
    sys.exit(1)

cast = chromecasts[0]
# Start socket client's worker thread and wait for initial status update
cast.wait()

yt = YouTubeController()
cast.register_handler(yt)
yt.play_video(VIDEO_ID)
#time.sleep(10)

#media = MediaController()
#cast.register_handler(media)
#media.stop()
