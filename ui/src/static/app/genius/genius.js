angular.module('genius', []).controller('geniusController', function(
  $scope, $routeParams, authState, api, $log
) {

  $scope.title = 'genius';

  var geniusId = $routeParams.geniusId;
  $log.debug('genius:', geniusId);

  $scope.authState = authState;
  $log.debug('authState', authState);
  
  api.users_detail.get({userId: geniusId}, function (data) {
    $log.debug('user detail:', data);
    $scope.user = data;
  });

});
