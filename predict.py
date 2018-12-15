import os
import argparse

from PIL import Image
from yolo import YOLO, detect_video


def detect_img(yolo, input_path, output_path):
    "Detect model items in the image"

    if not os.path.exists(output_path):
        os.mkdir(output_path)

    # If input is a folder predict all the content images
    if os.path.isdir(input_path):
        files = os.listdir(input_path)
        for imagefile in files:
            try:
                image = Image.open(os.path.join(input_path, imagefile))
            except:
                print('Open error ' + imagefile)
            else:
                r_image = yolo.detect_image(image, imagefile)
                r_image.save(output_path + imagefile)
        yolo.close_session()

    # If input is a .txt list predict all elements
    elif input_path.endswith('.txt'):
        image_paths = []

        with open(input_path) as f:
            lines = f.readlines()
            for line in lines:
                path=line.split(' ')[0]
                image_paths += [path]

            for input_img in image_paths:
                image_name = input_img.split('/')[-1]
                print(input_img)
                try:
                    image = Image.open(input_img)
                except:
                    print('Open error ' + input_img)
                else:
                    r_image = yolo.detect_image(image, image_name)
                    # r_image.show()
                    r_image.save(output_path + image_name)
            yolo.close_session()

    # If input is a file predict over file
    else:
        image_name = input_path.split('/')[-1]
        try:
            image = Image.open(input_path)
        except:
            print('open error! try again!')
        else:
            r_image = yolo.detect_image(image, image_name)
            r_image.show()
    yolo.close_session()

FLAGS = None

if __name__ == '__main__':
    # class YOLO defines the default value, so suppress any default here
    parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
    '''
    Command line options
    '''
    parser.add_argument(
        '--model', type=str,
        help='path to model weight file, default ' + YOLO.get_defaults("model_path")
    )

    parser.add_argument(
        '--anchors', type=str,
        help='path to anchor definitions, default ' + YOLO.get_defaults("anchors_path")
    )

    parser.add_argument(
        '--classes', type=str,
        help='path to class definitions, default ' + YOLO.get_defaults("classes_path")
    )

    parser.add_argument(
        '--gpu_num', type=int,
        help='Number of GPU to use, default ' + str(YOLO.get_defaults("gpu_num"))
    )

    parser.add_argument(
        '--image', default=False, action="store_true",
        help='Image detection mode'
    )
    parser.add_argument(
        "--input", nargs='?', type=str,required=False,default='./predict_inputs',
        help = "Content input path"
    )
    parser.add_argument(
        "--output", nargs='?', type=str, default="./predict_outputs",
        help = "[Optional] Content output path"
    )

    FLAGS = parser.parse_args()

    if FLAGS.image:
        """
        Image detection mode, disregard any remaining command line arguments
        """
        print("Image detection mode")
        detect_img(YOLO(**vars(FLAGS)), FLAGS.input, FLAGS.output)
    elif "input" in FLAGS:
        detect_video(YOLO(**vars(FLAGS)), FLAGS.input, FLAGS.output)
    else:
        print("Must specify at least video_input_path.  See usage with --help.")
