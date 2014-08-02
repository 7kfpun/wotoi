angular.module('admin', []).controller('adminController', function($scope, api) {

  $scope.title = 'admin';

  // create a message to display in our view
  $scope.message = 'Everyone come and see how good I look!';

  $scope.api = api;

  api.users_detail.get({userId: '123'}, function (data) {
    console.log(data);
    $scope.user_detail = data;
  });

});
