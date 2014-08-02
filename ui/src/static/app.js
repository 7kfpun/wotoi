// create the module and name it scotchApp
angular.module('app', [
  'ngRoute',
  'ngResource', 
  'ui.bootstrap',

  // Top level modules only
  'main',
  'login',
  'admin'
])

.config(['$httpProvider', function($httpProvider){

  $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
  $httpProvider.defaults.xsrfCookieName = 'csrftoken';

}])

.service('authState', function () {
  return {
    user: undefined
  };
})

// configure routes
.config(function($routeProvider) {

  $routeProvider

  .when('/', {
    templateUrl : 'static/app/main/main.tpl.html',
    controller  : 'mainController'
  })

  .when('/about', {
    templateUrl : 'static/app/about/about.tpl.html',
    controller  : 'aboutController'
  })

  .when('/services', {
    templateUrl : 'static/app/about/about.tpl.html',
    controller  : 'aboutController'
  })

  .when('/contact', {
    templateUrl : 'static/app/about/about.tpl.html',
    controller  : 'aboutController'
  })

  .when('/login', {
    templateUrl : 'static/app/login/login.tpl.html',
    controller  : 'loginController'
  })

  .when('/signup', {
    templateUrl : 'static/app/signup/signup.tpl.html',
    controller  : 'signupController'
  })

  .when('/admin', {
    templateUrl : 'static/app/admin/admin.tpl.html',
    controller  : 'adminController'
  });
});
