console.log("hello world")


function add_to_cart_view($this){
	var pk = $this.dataset.pk

	console.log('productPk: ', pk, 'Action:', action)
	console.log('USER: ', user)
	
	console.log('page: ', pageid)

	if (user == 'AnonymousUser'){
		LoginSignUpFunction(pk)
		console.log("User is not logged in")
	}else{
		console.log("User is logged in")
		updateUserOrder(pk, action, pageid)
	}	
}


function updateUserOrder(pk, action, pageid){
	console.log('User is authenticated, sending data...')

	var url = '/ajax/cart/detail/'

	fetch(url, {
		method:'POST',
		headers:{
			'Content-Type':'application/json',
			'Accept': 'application/json',
			'X-CSRFToken':csrftoken,
		}, 
		body:JSON.stringify({'pk':pk, 'action':action, 'pageid':pageid})
	})
	.then((response) => {
	   return response.json();
	})
	.then((data) => {
		var notif_tag = document.getElementById('AlreadyAdded'+pk.toString());
	
		if(pageid == "cart-page"){
			location.reload()
		}
		// location.reload()
		console.log("action: ", data["done_action"])
		// {"added":False, "removed":False, "cleared":False, "new_added":False}
		if (notif_tag != null){
			if (data["added"] == true && pageid == "product-page"){
				// alert("New product added to your cart.")
				notif_tag.innerHTML = 'Added To Cart';
				notif_tag.classList.toggle("show");
				// $('#AlreadyAdded'+productPk.toString()).hide(5000);
				// added_to_cart()
			}
			if (data["already_added"] == true && pageid == "product-page"){
				// alert("This product was already added to your cart.")
				notif_tag.innerHTML = 'Already Added';
				notif_tag.classList.toggle("show");
				// $('#AlreadyAdded'+productPk.toString()).hide(5000);
			}
		}
	});
}

// When the user clicks on div, open the popup
function LoginSignUpFunction(pk) {
	console.log("This method works fine")
	var popup = document.getElementById("PopupNotification"+pk.toString());
	popup.classList.toggle("show");
	// $('#PopupNotification'+productPk.toString()).hide(5000);
  }


function product_price($this){
	var price = $this.dataset.price;
	var price_info = $this.dataset.priceinfo;
	var display_price = document.getElementById("ProductPrice");
	var display_price_info = document.getElementById("ProductPriceInfo");
	display_price.innerHTML = price;
	display_price_info.innerHTML = price_info;

	console.log(price, price_info);
}


// control checkbox in cart page
function model_checkbox($this){
	var pk = $this.dataset.pk;
	var checkbox;
	var action = 'None';
	if (pk == 'all'){
		checkbox = document.getElementById('all_checkbox');
		if (checkbox.checked){
			action = 'checked';
		}else{
			action = 'unchecked';
		}
	}else{
		id = document.getElementById('model_checkbox'+toString(pk));
	}
	console.log(action);

	console.log(pk)
	model_checkbox_helper(pk, action)
	// $.ajax({
	// 	type: 'GET',
	// 	url: "/ajax/model/checkbox/",
	// 	data : { 
	// 		request_data: pk,
	// 	},
	// 	success: function(response) {
	// 		var instance = JSON.parse(response["instance"]);
	// 		console.log("Sellected: ", instance.length)

	// 		if (instance.length > 0){
	// 			for (var i = 0; i < instance.length; i++){
    //            console.log("pk: ",           instance[i]['pk'])
	// 				console.log("model_file: ",   instance[i]['fields']['model_file'])
    //            console.log("image: ",        instance[i]['fields']['image'])
    //            console.log("video_file: ",   instance[i]['fields']['video_file'])
    //            console.log("video_link: ",   instance[i]['fields']['video_link'])
    //            console.log("caption: ",      instance[i]['fields']['caption'])
    //            console.log("name: ",         instance[i]['fields']['name'])
    //            console.log("slug: ",         instance[i]['fields']['slug'])
    //            console.log("paid: ",         instance[i]['fields']['paid'])
    //            console.log("price: ",        instance[i]['fields']['price'])
    //            console.log("published_at: ", instance[i]['fields']['published_at'])
    //            console.log("updated_at: ",   instance[i]['fields']['updated_at'])
	// 			}
	// 		}
		
	// 	},
	// 	error: function() { 
	// 		console.log('Houston, we have a problem!');
	// 	}
	// });
}

function model_checkbox_helper(pk, action){
	console.log('User is authenticated, sending data...')

	var url = '/ajax/model/checkbox/'

	fetch(url, {
		method:'POST',
		headers:{
			'Content-Type':'application/json',
			'Accept': 'application/json',
			'X-CSRFToken':csrftoken,
		}, 
		body:JSON.stringify({'pk':pk, 'action':action})
	})
	.then((response) => {
	   return response.json();
	})
	.then((data) => {
		// var notif_tag = document.getElementById('AlreadyAdded'+pk.toString());
	});
}