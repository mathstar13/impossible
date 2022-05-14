# Impossible: A way to encode everything
## Installation
```
pip install impossible
```
## Usage
### impossible.encode(txt,key=False,ek="")
*txt: The text you wish to encode*

*key: Whether or not to return the entire string or to split it into the value and the key. Defalt: False (Return entire String).*

*ek: The key used to encode the string. If there is none, it will generate one.*

```python
impossible.encode("test")
# EX: -> bpf2vbpijvbpfsvbpf2,cotbg9rkqjilf8me56w,2n0yp4x3s017vhduza,nda09qegp56z71ktsrbj4uioxhfl3cy2,wv08ml,
```

```python
impossible.encode("test",key=True)
# EX: -> ['la7vmla9bmla74mla7v', 'rgvc95dfkmawq13s0lytu4zjbx70o,en6hi2p8,jz4b6fguc,xplhe9d0knr3ws5m7iv810qt2aoy,']
```

```python
impossible.encode("test",ek="4wyx6i0fz3nkms1elurgtjb2d7oqc9vpa8h5,.tpmocnes5y,kardh17glx6qvibf4j308w9u2z.")
# -> vtuqnvtjznvtu9nvtuq.4wyx6i0fz3nkms1elurgtjb2d7oqc9vpa8h5,.tpmocnes5y,kardh17glx6qvibf4j308w9u2zl.
```
### impossible.encodeShort(txt,key=False,ek="",ssc=' !"#$%&\'()*,-./0123456+789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_\`abcdefghijklmnopqrstuvwxyz{|}~®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþ',uus=True)
