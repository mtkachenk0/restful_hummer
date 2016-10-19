"""
An example of API doc, I'd like to assure you I've read about that.
But the thing is Django-rest-framework have its own Documentation tool
"""
"""
 * @api {get} /user/<id> Get User By ID
 * @apiVersion 0.1.0
 * @apiName GetUser
 * @apiGroup User
 * @apiPermission admin
 * @apiDescription Try it:
    http://127.0.0.1:8000/users/1

 * @apiParam {Number} id The Users-ID.

 * @apiExample Example usage:
       curl -u user:password -i http://host:port/users/<pk>/

 * @apiSuccess {Number}   id            The Users-ID.
 * @apiSuccess {String}   username      Username.
 * @apiSuccess {Number[]} items         Item IDs created by User.
 * @apiSuccess {String}   email         User email.
 * @apiSuccess {SHA}      password      Encrypted user password.

 * @apiSuccessExample {json} Response Example:
    {
        "id":2,
        "username":"admin",
        "items":[],
        "email":"admin@gmail.com",
        "password":"pbkdf2_sha256$30000$JY9Cge2olIxq$hSZlZx0YNUmdCq71wpbMHfFqW/wC+3nGfRv71MTgYHQ="
    }
 * @apiUse 404
 * @apiUse 403
"""

"""
 * @api {get} /users/ Get Users
 * @apiVersion 0.1.0
 * @apiName GetUsers
 * @apiGroup User
 * @apiPermission admin
 * @apiDescription Try it:
    http://127.0.0.1:8000/users/

 * @apiExample Example usage:
       curl -u user:password -i http://host:port/users/

 * @apiSuccess {Array[]}  users                 List of Users (Array of Objects).
 * @apiSuccess {Object[]} users.user            User object.
 * @apiSuccess {Number}   users.user.id         The Users-ID.
 * @apiSuccess {String}   users.user.username   User Name.
 * @apiSuccess {Number[]} users.user.items      Items created by User.
 * @apiSuccess {String}   users.user.email      User email.
 * @apiSuccess {SHA}      users.user.password   Encrypted user password.

 * @apiUse 403
 * @apiSuccessExample {json} Response Example:
    [{
        "id":2,
        "username":"admin",
        "items":[],
        "email":"admin@gmail.com",
        "password":"pbkdf2_sha256$30000$JY9Cge2olIxq$hSZlZx0YNUmdCq71wpbMHfFqW/wC+3nGfRv71MTgYHQ="
      },{
        "id":1,
        "username":"mtkachenko",
        "items":[2,3,4,5,6,7],
        "email":"",
        "password":"pbkdf2_sha256$30000$HtpEULLAFVnk$0csDW0QMw46AR/r6n9ufkDVgaiugt/5HWUPCS5rynQQ="
    }]
"""