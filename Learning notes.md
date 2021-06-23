# Learned
## 1. To redirect with arguments use:
```py
kwargs = {'x': x,'y':y}
        
	return redirect( 'CrossTable:setup1',**kwargs)
```
## 2. Difference between request.POST.get('roofbite') and request.POST('roofbite')

request.POST('roofbite') will raise a KeyError exception if 'roofbite' is not in request.POST.
request.POST.get('roofbite') will return None

request.POST.get has also default option:
``` py
request.POST.get('roofbite','lack of roofbite')
```
## 3. To do html input in loop 
You should use tag 
``` html
<fieldset></fieldset>
```
inside form

# Debuging

## 1. `Don't mix *args and **kwargs in call to reverse()!`
 Error occured when I've passed request in return reverse()

## 2. Html form was not sending data
I've closed <form> tag too early in code and got error 
`CSRF verification failed. Request aborted. (Forbidden (403)) DJANGO`

## 3.  request.POST.get should have () not {}
Proper: 
```py
 request.POST.get('questions_number')
 ```

 ## 4. Remember about coomas between paths in urlpatterns!!