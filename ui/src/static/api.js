// // API
// angular.module('app').factory('User', [
  // '$resource', function($resource) {
    // return $resource('/api/v1/users/:username', {
      // username: '@username'
    // });
  // }
// ])

// .factory('Job', [
  // '$resource', function($resource) {
    // return $resource('/api/v1/jobs/:id', {
      // id: '@id'
    // });
  // }
// ])

// .factory('Photo', [
  // '$resource', function($resource) {
    // return $resource('/api/v1/photos/:id', {
      // id: '@id'
    // });
  // }
// ]);

angular.module('app').factory('api', function($resource){
  function add_auth_header(data, headersGetter){
    var headers = headersGetter();
    headers['Authorization'] = ('Basic ' + btoa(data.username +
                                                ':' + data.password));
  }
  return {
    auth: $resource('/api/v1/auth\\/', {}, {
      login:  {method: 'POST', transformRequest: add_auth_header},
      logout: {method: 'DELETE'}
    }),
    users: $resource('/api/v1/users\\/', {}, {
      list:   {method: 'GET', isArray: true},
      create: {method: 'POST'}
    }),
    users_detail: $resource('/api/v1/users/:userId\\/', {userId:'@id'}, {
      get:    {method: 'GET'}
    }),
    jobs: $resource('/api/v1/jobs\\/', {}, {
      list:   {method: 'GET', isArray: true},
      create: {method: 'POST'},
      detail: {method: 'GET', url: '/api/posts/:id'},
      delete: {method: 'DELETE', url: '/api/posts/:id'}
    })
  };
})
