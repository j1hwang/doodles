function AddressBook() {
	this.contacts = [];
	this.initialComplete = false;
}

AddressBook.prototype.getInitialContacts = function(cb) {
	var self = this;

	setTimeout(function() {
		self.initialComplete = true;
		if(cb) {
			return cb();
		}
	}, 10);
}

AddressBook.prototype.addContact = function(contact) {
	this.contacts.push(contact);
};

AddressBook.prototype.getContact = function(idx) {
	return this.contacts[idx];
}

AddressBook.prototype.deleteContact = function(idx) {
	this.contacts.splice(idx, 1);
}