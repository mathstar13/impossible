# Impossible: A way to encode everything
## Installation
```
pip install impossible
```
## Usage
### Simple Example
```python
import impossible
encoded_string = impossible.encode("Hello World!")
print(encoded_string)
decoded_string = decode(encoded_string)
print(decoded_string)
```
### Using Keys
To use a key, first you must generate it.
```python
import impossible
key = impossible.generate_key()
print(key)
# -> 9,ogwje68zm5kcsbxl0yrf4d2731qauptinhv.m8hzqsbvx,lketd4ca0wgpjyu691ir725onf3.
```

Then, you can encode and decode using that key.
```python
import impossible
encoded_value = impossible.encode("Hello World",ek="9,ogwje68zm5kcsbxl0yrf4d2731qauptinhv.m8hzqsbvx,lketd4ca0wgpjyu691ir725onf3.",key=True)[0]
print(encoded_value)
decoded_value = decode(encoded_value,key="9,ogwje68zm5kcsbxl0yrf4d2731qauptinhv.m8hzqsbvx,lketd4ca0wgpjyu691ir725onf3.")
print(decoded_value)
```
