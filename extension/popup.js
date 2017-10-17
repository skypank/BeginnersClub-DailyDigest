document.addEventListener('DOMContentLoaded', function() {
  var likePageButton = document.getElementById('likePage');
  var okokPageButton = document.getElementById('okokPage');
  var dislikePageButton = document.getElementById('dislikePage');
  
  likePageButton.addEventListener('click', function() {

    chrome.tabs.getSelected(null, function(tab) {
     alert(tab.url);
    });
  }
  , false);
}, false);