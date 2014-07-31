angular.module('about', []).controller('aboutController', ['$scope', function($scope) {

  $scope.title = 'about';

  // create a message to display in our view
  $scope.message = 'Everyone come and see how good I look!';
}]);
