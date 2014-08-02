angular.module('main', []).controller('mainController', function($scope, api, authState, $log) {

  $scope.title = 'main';

  $scope.api = api;

  $scope.list = function() {
    api.jobs.list(function(data) {
      $log.debug('jobs', data);
      $scope.jobs = data;
    });

    api.users.list(function(data) {
      $log.debug('geniuses:', data);
      $scope.geniuses = data;
    });
  };
  $scope.list();

});
