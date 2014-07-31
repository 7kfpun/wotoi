angular.module('job', []).controller('jobController', ['$scope', function($scope) {

  $scope.title = 'job';

  // create a message to display in our view
  $scope.message = 'Everyone come and see how good I look!';
}]);
