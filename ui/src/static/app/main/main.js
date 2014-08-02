angular.module('main', []).controller('mainController', function($scope, api, authState) {

  $scope.title = 'main';

  // create a message to display in our view
  $scope.message = 'Everyone come and see how good I look!';

  $scope.list = function(){
    api.jobs.list(function(data){
      $scope.jobs = data;
    });
  };
  $scope.list();

});
