# Rbxthon

Rbxthon is an Open-Source Roblox API built using Python

Why should you use Rbxthon:
- Rbxthon offers amazing documentation
- Rbxthon is super easy to use
- We're open-source

> Visit our github [here](https://github.com/gordxn/RbxThon)


# Documentation

## User


### UsernameById(id)
> Type: **GET** <br>
> Args: id - The ID of the user that you want the Username of;
> <br>
> #### Returns the Username of the player with given Id <br>
> ### Errors
> Invalid Id <br>
> User not found <br>
> ### Usage
> ```python
> from rbxthon import User
> 
> def UserById(id):
> 	print(User.UsernameById(id))
> 
> UserById(116297738)

### IdByUsername(id)
> Type: **GET** <br>
> Args: username - The Username of the user that you want the ID of;
> <br>
> #### Returns the Id of the player with given username <br>
> ### Errors
> Invalid username <br>
> User not found <br>
> ### Usage
> ```python
> from rbxthon import User
> 
> def IdByUser(username):
> 	print(User.IdByUsername(username))
> 
> IdByUser("GordxnHxyward20")

`This is possible thanks to https://api.roblox.com/docs`
