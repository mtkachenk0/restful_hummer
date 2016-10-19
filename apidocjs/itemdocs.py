"""
 * @apiDefine 403
 *   @apiError Forbidden(403) Only authenticated Admins can modify data.
"""
"""
 * @apiDefine 400
 *   @apiError BadRequest(400) Wrong, incorrect request.
"""
"""
 * @apiDefine 404
 *   @apiError NotFound(404) Item not found.
"""
"""
 * @apiDefine 409
 *   @apiError Conflict(409) Conflict.
"""

# ItemList GetAll
"""
 * @api {get} /items/ Get All Items
 * @apiVersion 0.1.0
 * @apiName GetItems
 * @apiGroup Item
 * @apiPermission no-auth

 * @apiDescription Try it:
    http://127.0.0.1:8000/items/
 * @apiExample Example usage:
       curl http://host:port/items/

 * @apiSuccess {Array[]}  items                 List of Items (Array of Objects).
 * @apiSuccess {Object[]} items.item            Item object.
 * @apiSuccess {Number}   items.item.id         The Item-ID.
 * @apiSuccess {String}   items.item.name       Item Name.
 * @apiSuccess {Number}   items.item.price      Item Price.
 * @apiSuccess {Number[]} items.item.categories Categories Item belongs to.
 * @apiSuccess {DateTime} items.item.created    Date created
 * @apiSuccess {String}   items.item.owner      Owner Username

 * @apiSuccessExample {json} Response:
    [{
      "id": 1,
      "name": "vasabi",
      "price": "43.31",
      "categories": [4,5],
      "created": "2016-10-18T15:28:36.640547Z",
      "owner": "mtkachenko"}, ...
    ]}
 * @apiUse 400
 """

# ItemList Create
"""
 * @api {post} /items/ Create Item
 * @apiVersion 0.1.0
 * @apiName CreateItem
 * @apiGroup Item
 * @apiPermission auth
 * @apiDescription Try it:
    http://127.0.0.1:8000/items/

 * @apiParam {String}      name           Item Name.
 * @apiParam {Number}      price          Item Price.
 * @apiParam {Number[]}    categories     Categories Item belongs to.

 * @apiExample Example usage:
       curl -X POST -u user:password http://host:port/items/ --data "name=arg1&price=arg2&categories=arg3&categories=arg4"

 * @apiSuccess {Object[]} item            Item object.
 * @apiSuccess {Number}   item.id         The Item-ID.
 * @apiSuccess {String}   item.name       Item Name.
 * @apiSuccess {Number}   item.price      Item Price.
 * @apiSuccess {Number[]} item.categories Categories Item belongs to.
 * @apiSuccess {DateTime} item.created    Date created
 * @apiSuccess {String}   item.owner      Owner Username

 * @apiSuccessExample {json} Response:
    {
      "id":7,
      "name":"test",
      "price":"30.00",
      "categories":[4,5],
      "created":"2016-10-18T23:17:32.001848Z",
      "owner":"mtkachenko"
    }

 * @apiUse 400
 * @apiUse 409
"""

# ItemDetail GetByID
"""
 * @api {get} /items/<pk> Get Item By ID
 * @apiVersion 0.1.0
 * @apiName GetItem
 * @apiGroup Item
 * @apiPermission no-auth
 * @apiDescription Try it:
    http://127.0.0.1:8000/items/1

 * @apiParam {Number} id The Item-ID.

 * @apiExample Example usage:
       curl -i http://host:port/items/<pk>/


 * @apiSuccess {Object[]} item            Item object.
 * @apiSuccess {Number}   item.id         The Item-ID.
 * @apiSuccess {String}   item.name       Item Name.
 * @apiSuccess {Number}   item.price      Item Price.
 * @apiSuccess {Number[]} item.categories Categories Item belongs to.
 * @apiSuccess {DateTime} item.created    Date created
 * @apiSuccess {String}   item.owner      Owner Username

 * @apiUse 404
"""

# ItemDetail UpdateByID
"""
 * @api {put} /items/<pk> Update Item
 * @apiVersion 0.1.0
 * @apiName UpdateItem
 * @apiGroup Item
 * @apiPermission auth
 * @apiDescription Try it:
    http://127.0.0.1:8000/items/1

 * @apiParam {Number}      id             Item ID.
 * @apiParam {String}      name           Item Name.
 * @apiParam {Number}      price          Item Price.
 * @apiParam {Number[]}    categories     Categories Item belongs to.

 * @apiExample Example usage:
       curl -X PUT -u user:password http://host:port/items/<pk>/ --data "name=arg1&price=arg2&categories=arg3&categories=arg4"

 * @apiSuccess {Object[]} item            Item object.
 * @apiSuccess {Number}   item.id         The Item-ID.
 * @apiSuccess {String}   item.name       Item Name.
 * @apiSuccess {Number}   item.price      Item Price.
 * @apiSuccess {Number[]} item.categories Categories Item belongs to.
 * @apiSuccess {DateTime} item.created    Date created
 * @apiSuccess {String}   item.owner      Owner Username

 * @apiSuccessExample {json} Response Example
    {
        "id":2,
        "name":"vasabi",
        "price":"30.00",
        "categories":[4,5],
        "created":"2016-10-18T16:02:14.508570Z",
        "owner":"mtkachenko"
    }

 * @apiUse 403
 * @apiUse 404

"""
# ItemDetail DeleteByID
"""
 * @api {delete} /items/:id Delete Item
 * @apiVersion 0.1.0
 * @apiName DeleteItem
 * @apiGroup Item
 * @apiPermission auth
 * @apiDescription Try it:
    http://127.0.0.1:8000/items/1

 * @apiParam {Number}      id             Item ID.

 * @apiExample Example usage:
       curl -X DELETE -u user:password -i http://host:port/items/<pk>/

 * @apiSuccessExample  Response Example
    HTTP/1.0 204 No Content
    Date: Tue, 18 Oct 2016 22:54:19 GMT
    Server: WSGIServer/0.2 CPython/3.4.3+
    Vary: Accept, Cookie
    X-Frame-Options: SAMEORIGIN
    Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS

 * @apiUse 403
 * @apiUse 404
"""