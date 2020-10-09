window.onload = function () {
    var modal = document.getElementById("modalWindow")
    var buttonFindFriendModal = document.getElementById("findFriend")

    buttonFindFriendModal.onclick = function () {
        window.alert("clicked")
        modal.style.display = "block"
    }

    window.onclick = function () {
        if (event.target == modal) {
            modal.style.display = "none"
        }
    }
}
