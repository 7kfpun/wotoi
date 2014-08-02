// create the module and name it scotchApp
angular.module('app', [
  'ngRoute',
  'ngResource', 
  'ui.bootstrap',
  'ngCookies',
  'ipCookie',

  // Top level modules only
  'main',
  'admin',
  'login',
  'signup',

  'job',
  'genius'
])

.config(function($httpProvider, $logProvider){

  $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
  $httpProvider.defaults.xsrfCookieName = 'csrftoken';

  $logProvider.debugEnabled(true);
})

.service('authState', function (ipCookie) {
  return {
    user: ipCookie('user') || undefined
  };
})

.service('config', function ($rootScope, $log, ipCookie) {
  config = {
    debug: ipCookie('debug') || true
  };

  if (config.debug) {
    $log.info("config", config);
  }

  $rootScope.config = config;
  return config;
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

  .when('/genius', {
    templateUrl : 'static/app/genius/genius_markup.tpl.html',
    controller  : 'geniusController'
  })

  .when('/genius/:geniusId/', {
    templateUrl : 'static/app/genius/genius.tpl.html',
    controller  : 'geniusController'
  })

  .when('/admin', {
    templateUrl : 'static/app/admin/admin.tpl.html',
    controller  : 'adminController'
  });
});
