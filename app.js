(function(){

  var app = angular.module('notesApp', []);
  app.controller('NotesController', function($scope){
    $scope.notes = notes;
    $scope.activeNoteNum = 0;
    //$scope.activeNote = notes[$scope.activeNoteNum];
    $scope.activeNote = angular.copy(notes[$scope.activeNoteNum]);
    $scope.onSave = function(){
      alert('Saved');
    };
    $scope.onClear = function(){
      $scope.activeNote.text = "";
    };
    $scope.setNote = function(noteId){
      $scope.activeNoteNum = noteId;
      $scope.activeNote = angular.copy(notes[$scope.activeNoteNum]);
    };
  });

  var note1 = {
    id: 0,
    text: "abc",
  };
  var note2 = {
    id: 1,
    text: "Note2",
  };
  var note3 = {
    id: 2,
    text: "Note3",
  };

  var notes = [note1, note2, note3];
}());
