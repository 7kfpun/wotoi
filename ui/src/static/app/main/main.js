angular.module('main', []).controller('mainController', ['$scope', 'Job', 'User', function($scope, Job, User) {

  $scope.title = 'main';

  // create a message to display in our view
  $scope.message = 'Everyone come and see how good I look!';

  $scope.users = User.query();
}]);
