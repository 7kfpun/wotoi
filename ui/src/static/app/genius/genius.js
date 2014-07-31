angular.module('genius', []).controller('geniusController', ['$scope', function($scope) {

  $scope.title = 'genius';

  // create a message to display in our view
  $scope.message = 'Everyone come and see how good I look!';
}]);
