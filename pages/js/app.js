var app = angular.module("SocModule", ["ngRoute"]);

app.config(function($routeProvider) {
    $routeProvider
    .when("/", {
        templateUrl : "index.htm"
    })
    .when("/signin", {
        templateUrl : "signin.htm"
    })
    .when("/posts", {
        templateUrl : "posts.htm"
    })
});

app.controller("UserController", function ($scope, $http) {
    $scope.users = [];
    $scope.data = {
        username: "",
        email: "",
        password: ""
    };
    
    $scope.sign_up = function () {
        var method = "POST";
        var url = "http://localhost:8000/users/";

        var params = JSON.stringify($scope.data);

        $http({
            method: method,
            url: url,
            data: params,
            headers: {'Content-Type':'application/json'}
        }).then(_success, _error)
        
    };

    $scope.sign_in = function () {
        var method = "POST";
        var url = "http://localhost:8000/auth/";

        var params = JSON.stringify({username: $scope.data.username, password: $scope.data.password});

        $http({
            method: method,
            url: url,
            data: params,
            headers: {'Content-Type':'application/json'}
        }).then(_success, _error)
    };

    $scope.logout = function () {
        document.cookie = "token=; Expires=Thu, 01 Jan 1970 00:00:01 GMT;";
        window.location.replace("http://localhost:8000/signin")
    };

    function _success(response) {
        token = response.data.token;
        document.cookie = "token=" + token;
        window.location.replace("http://localhost:8000/posts")
    }

    function _error(repsonse) {
        console.log(response.statusText)

    }
});


app.controller("PostsController", function ($scope, $http) {
    $scope.posts = [];
    $scope.data = {
        post_id : -1,
        title: "",
        description: ""
    };

    _refreshPosts();



    function _refreshPosts(){
        $http({
            method: "GET",
            url: "http://localhost:8000/posts/"
        }).then(function successCallback(response) {
            $scope.data = response.data;

        }, function errorCallback(response) {
            console.log(response.statusText)

        })
    }
    
    $scope.submit_post = function () {
        var method = "POST";
        var url = "http://localhost:8000/posts/";

        var params = JSON.stringify({user: document.cookie, title: $scope.data.title, description: $scope.data.description});

        $http({
            method: method,
            url: url,
            data: params,
            headers: {'Content-Type':'application/json'}
        }).then(_refreshPosts())
        
    };

    $scope.submit_like = function () {
        var method = "POST";
        var url = "http://localhost:8000/likes/" + $scope.data.post_id;

        var params = JSON.stringify({token: document.cookie});

        $http({
            method: method,
            url: url,
            data: params,
            headers: {'Content-Type':'application/json'}
        }).then(_refreshPosts())
    }

});
