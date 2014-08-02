angular.module('admin', []).controller('adminController', function($scope, authState, api, $log, config) {
  
  $scope.title = 'admin';

  $scope.config = config;

  $scope.authState = authState;
  $log.debug('authState', authState);

  $scope.api = api;

  api.users_detail.get({userId: authState.user}, function (data) {
    $log.debug('user detail:', data);
    $scope.user = data;
  });

  api.config.languages.list(function (data) {
    $log.debug('languages:', data);
    $scope.languages = data;
  });

});
