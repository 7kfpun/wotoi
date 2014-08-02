angular.module('login', []).controller('loginController', function($scope, $rootScope, api, authState) {

  $scope.title = 'login';

  // create a message to display in our view
  $scope.message = 'Everyone come and see how good I look!';

  $scope.authState = authState;

  $scope.getCredentials = function(){
    return {username: $scope.username, password: $scope.password};
  };

  $scope.api = api;

  $scope.login = function(){
    api.auth.login($scope.getCredentials()).
      $promise.
      then(function(data){
      authState.user = data.username;
    })
    .catch(function(data){
      alert(data.data.detail);
    });
  };

  $scope.logout = function(){
    api.auth.logout(function(){
      authState.user = undefined;
    });
  };

  $scope.register = function($event){
    $event.preventDefault();
    api.users.create($scope.getCredentials()).
      $promise.
      then($scope.login).
      catch(function(data){
      alert(data.data.username);
    });
  };

});
