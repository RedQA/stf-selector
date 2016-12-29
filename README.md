# stf-selector

The stf-selector package is designed for supporting query available mobile devices through STF restful api with flexible conditions.
 
## Getting Started

### Installing stf-selector

To install **stf-selector** from PyPI, run:

	$ pip install stf-selector

You can also grab the latest development version from [GitHub][github]. After downloading and unpacking it, you can install it using:

[github]: https://github.com/RedQA/stf-selector

	$ python setup.py install

## STF
Because stf-selector is based on the [STF] '(Smartphone Test Farm)', you should install **STF** firstly and then read the [STF API]. If you already know the stf, I suggest you skip to this.

[STF]: https://github.com/openstf/stf
[STF API]: https://github.com/openstf/stf/blob/master/doc/API.md

STF project and api document are avaliable from below:

*STF github: <https://github.com/openstf/stf>  

*STF API: <https://github.com/openstf/stf/blob/master/doc/API.md>


## Usage
According to STF API, you need get token firstly. If you don't know how to get token, please refer to [Authentication]. 

[Authentication]: https://github.com/openstf/stf/blob/master/doc/API.md#authentication
``` python	
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from stf_selector.selector import Selector
from stf_selector.query import where
	
# Your STF's url, like: https://stf.example.org/api/v1/user
url = ""
# Token genereated from the STF, some like:"3e5dd447c..."
token = "" 
```

### Example Code
#### Basic usage
Get all the devices on the STF

```python
s = Selector(url=url, token=token)
device_list = s.load().devices()
```

#### Query Language
Search for a field value

```python
s = Selector(url=url, token=token)
s.load()
device_list = s.find(where("manufacturer")=="SAMSUNG").devices()
```

**Note:** 	
Because the devices on the STF can be used many people at the same time, which results in devices using or releasing at any time, you need **refresh()** at appropriate frequency. 
	
Search with combing two queries with logical '&' or 'and'.
	
```python
s = Selector(url=url, token=token)
s.load()
conds = (where("manufacturer")=="SAMSUNG") & (where('version')=='5.0')
device_list = s.find(conds).devices()
```

**Note:**		
When using & or |, make sure you wrap the conditions on both sides with parentheses or Python will mess up the comparison.

Search with combing two queries with logical '|' or 'or'.

```python
s = Selector(url=url, token=token)
s.load()
conds = (where("manufacturer")=="SAMSUNG") |(where("manufacturer")=="OPPO"))
device_list = s.find(cond=conds).devices()
# More possible comparisons: !=  <  >  <=  >=
```

#### More about query
You’ve learned about the basic comparisons (==, <, >, ...). In addition to these query supports the following queries:
	
 1. Existence of a 'field':
 	
 	``` python
 	s = Selector(url=url, token=token)
 	s.load()
 	s = s.find(where('sdk').exists())
 	```
 2. Regex:
 		
 	``` python
 	s = Selector(url=url, token=token)
 	s.load()
 	# return all model start with SM...
 	s = s.find(where('model').matches('SM*'))
 	```
 	
 3. Custom test:
	
	``` python	
	s = Selector(url=url, token=token)
 	s.load()
 	test_func = lambda x: x == '19'
	s = s.find(where('sdk').test(test_func))
 	```
 	
 4. Custom test with parameters:
 	
 	``` python
 	s = Selector(url=url, token=token)
 	s.load()
 	# return moblies which devices sdk is between m and n
 	def test_func(val, m, n):
 		 return int(m) <= int(val) <= int(n)
	s = s.find(where('sdk').test(test_func, 19, 21))
	```
		
 5. When a field contains a list, you also can use the following methods:
  	
  	``` python	
  	# Using a where:
  	s = Selector(url=url, token=token)
 	s.load()
 	
 	# Chrome is member of at least one of name groups
 	s = s.find(where('browser')['apps'].any(where('name')=='Chrome'))
 		
 	s.refresh()
 	# Chrome is only member of name groups
 	s = s.find(where('browser')['apps'].all(where('name')=='Chrome'))
 	```