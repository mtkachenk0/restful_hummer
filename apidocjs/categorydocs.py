# CategoryList GetAll
"""
 * @api {get} /categories/ Get All Categories
 * @apiVersion 0.1.0
 * @apiName GetCategories
 * @apiGroup Category
 * @apiPermission no-auth

 * @apiDescription Try it:
    http://127.0.0.1:8000/categories/
 * @apiExample Example usage:
       curl http://host:port/categories/

 * @apiSuccess {Array[]}  categories                                List of Categories (Array of Objects).
 * @apiSuccess {Object[]} categories.category                       Category object.
 * @apiSuccess {Number[]} categories.category.id                    Category-IDs.
 * @apiSuccess {String}   categories.category.name                  Category Name.
 * @apiSuccess {Number}   categories.category.parent_category       Parent Category ID.
 * @apiSuccess {DateTime} category.created                          Date created
 * @apiSuccess {String}   category.owner                            Owner Username


 * @apiSuccessExample {json} Response:
    [{
        "id":7,
        "name":"Car",
        "parent_category":5,
        "created":"2016-10-19T00:06:39.782367Z",
        "owner":"mtkachenko"
    },{
        "id":8,
        "name":"Carutsa",
        "parent_category":5,
        "created":"2016-10-19T00:08:39.782367Z",
        "owner":"mtkachenko"
    }]
 * @apiUse 400
 """

# CategoryList Create
"""
 * @api {post} /categories/ Create Category
 * @apiVersion 0.1.0
 * @apiName CreateCategory
 * @apiGroup Category
 * @apiPermission auth
 * @apiDescription Try it:
    http://127.0.0.1:8000/categories/

 * @apiParam {String}    name                 Category Name.
 * @apiParam {Number}    parent_category      The Parent Category-ID.

 * @apiExample Example usage:
       curl -X POST -u user:password http://host:port/categories/ --data "name=arg1&parent_category=arg3"

 * @apiSuccess {Object[]} category                    Category object.
 * @apiSuccess {String}   category.name               Category Name.
 * @apiSuccess {Number}   category.parent_category    The Parent Category-ID.
 * @apiSuccess {DateTime} category.created            Date created
 * @apiSuccess {String}   category.owner              Owner Username

 * @apiSuccessExample {json} Response:
    {
        "id":7,
        "name":"Car",
        "parent_category":5,
        "created":"2016-10-19T00:06:39.782367Z",
        "owner":"mtkachenko"
    }

 * @apiUse 400
 * @apiUse 409
"""

# CategoryDetail GetByID
"""
 * @api {get} /categories/<pk> Get Category By ID
 * @apiVersion 0.1.0
 * @apiName GetCategory
 * @apiGroup Category
 * @apiPermission no-auth
 * @apiDescription Try it:
    http://127.0.0.1:8000/categories/1

 * @apiParam {Number} id The Category-ID.

 * @apiExample Example usage:
       curl -i http://host:port/categories/<pk>/


 * @apiSuccess {Object[]} category                    Category object.
 * @apiSuccess {String}   category.name               Category Name.
 * @apiSuccess {Number}   category.parent_category    The Parent Category-ID.
 * @apiSuccess {DateTime} category.created            Date created
 * @apiSuccess {String}   category.owner              Owner Username

 * @apiSuccessExample {json} Response:
    {
        "id":7,
        "name":"Car",
        "parent_category":5,
        "created":"2016-10-19T00:06:39.782367Z",
        "owner":"mtkachenko"
    }

 * @apiUse 404
"""

# CategoryDetail UpdateByID
"""
 * @api {put} /categories/<pk> Update Category
 * @apiVersion 0.1.0
 * @apiName UpdateCategory
 * @apiGroup Category
 * @apiPermission auth
 * @apiDescription Try it:
    http://127.0.0.1:8000/categories/1

 * @apiParam {String}    name                 Category Name.
 * @apiParam {Number}    parent_category      The Parent Category-ID.

 * @apiExample Example usage:
       curl -X PUT -u user:password http://host:port/categories/<pk>/ --data "name=arg1&parent_category=arg3"

 * @apiSuccess {Object[]} category                    Category object.
 * @apiSuccess {String}   category.name               Category Name.
 * @apiSuccess {Number}   category.parent_category    The Parent Category-ID.
 * @apiSuccess {DateTime} category.created            Date created
 * @apiSuccess {String}   category.owner              Owner Username

 * @apiSuccessExample {json} Response:
    {
        "id":7,
        "name":"Car",
        "parent_category":5,
        "created":"2016-10-19T00:06:39.782367Z",
        "owner":"mtkachenko"
    }

 * @apiUse 403
 * @apiUse 404

"""
# CategoryDetail DeleteByID
"""
 * @api {delete} /categories/:id Delete Category
 * @apiVersion 0.1.0
 * @apiName DeleteCategory
 * @apiGroup Category
 * @apiPermission auth
 * @apiDescription Try it:
    http://127.0.0.1:8000/categories/1

 * @apiParam {Number}      id             Category ID.

 * @apiExample Example usage:
       curl -X DELETE -u user:password -i http://host:port/categories/<pk>/

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