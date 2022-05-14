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
```

Then, you can encode and decode using that key.
