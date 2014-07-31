angular.module('admin', []).controller('adminController', ['$scope', function($scope) {

  $scope.title = 'admin';

  // create a message to display in our view
  $scope.message = 'Everyone come and see how good I look!';
}]);
