# Image Exchange

I would really like this project to be used as a means of secure image exchange. Currently the program takes two keys to produce a permutation of the pixels within the image. It also uses a simple application of Fermats little theorem to distort the colours within the image. This is just a quick and dirty way of making it more difficult to piece the image together.

## Secure Exchange

We would like it to be possible to encrypt an image and send it to our friend so that anyone who intercepts the image is unable to decode it. Additionally it would be favourable if anybody who also intercepts the communication between my friend and I are unable to decode the image.

In order to successfully encrypt and decrypt the image my friend and I must agree upon two common keys. One fairly rudimental way to achieve this would be to use Diffie-Hellman protocol twice. Doing so we would establish two shared keys which are difficult for an attacker to recover.

# Ideas?

I would like to develop a cleaner way to produce a shared set of keys for the image exchange. It would be fantastic if each person could choose a single key and use these to construct a third shared key (through a method such as Diffie-Hellman). These keys could then be used in combination ot encrypt and decrypt the image. I need to do some work to figure out if that is possible.

If anyone reading this has suggestions for algorithms or reading material that may help it would be greatly appreciated!
