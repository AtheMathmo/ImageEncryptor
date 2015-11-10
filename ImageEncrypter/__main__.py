import sys, argparse

import image_crypt

parser = argparse.ArgumentParser(description='Encrypt and decrypt images.')


files = parser.add_mutually_exclusive_group(required=True)

files.add_argument('-e', '--encrypt', metavar='<encryptfile>',
	help='Path to image to encrypt.')

files.add_argument('-d', '--decrypt', metavar='<decryptfile>',
	help='Path to image to decrypt.')

parser.add_argument('-o', '--output', metavar='<outputfile>',
	default='output.png', help='Path to output file.\
	Defaults to "output.png".')

parser.add_argument('keys', type=int, nargs=2,
	help='Pair of keys.')

args = parser.parse_args()

# Now we should process the arguments and run the program.
if args.encrypt is not None:
	if args.output is None:
		image_crypt.encrypt_image(args.encrypt, args.keys[0], args.keys[1])
	else:
		image_crypt.encrypt_image(args.encrypt, args.keys[0], args.keys[1], args.output)

if args.decrypt is not None:
	if args.output is None:
		image_crypt.decrypt_image(args.decrypt, args.keys[0], args.keys[1])
	else:
		image_crypt.decrypt_image(args.decrypt, args.keys[0], args.keys[1], args.output)