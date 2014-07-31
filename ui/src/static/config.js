// API
angular.module('app').factory('User', [
  '$resource', function($resource) {
    return $resource('/api/v1/users/:username', {
      username: '@username'
    });
  }
])

.factory('Job', [
  '$resource', function($resource) {
    return $resource('/api/v1/jobs/:id', {
      id: '@id'
    });
  }
])

.factory('Photo', [
  '$resource', function($resource) {
    return $resource('/api/v1/photos/:id', {
      id: '@id'
    });
  }
]);
