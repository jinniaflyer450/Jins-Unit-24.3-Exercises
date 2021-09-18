const BASE_URL = 'http://localhost:5000' 


async function loadCupcakes(){
    const cupcakes = await axios.get(`${BASE_URL}/api/cupcakes`);
    for(let cupcake of cupcakes.data.cupcakes){
        const id = cupcake.id;
        const flavor = cupcake.flavor;
        const image = cupcake.image;
        const rating = cupcake.rating;
        $('#all-cupcakes').append
        (
            `<li class="cupcake" data-id=${id}><img src=${image}>${flavor}--${rating}/10</li>`
            );
        }
    }

$('#all-cupcakes').ready(loadCupcakes);

$('#add-cupcake-form').submit(
    async function(evt){
        evt.preventDefault();
        const $flavor = $('#flavor').val();
        const $size = $('#size').val();
        const $rating = $('#rating').val();
        const $image = $('#image').val();
        const newCupcake = await axios.post(`${BASE_URL}/api/cupcakes`, {'flavor': $flavor, 'size': $size, 
        'rating': $rating, 'image': $image});
        $('#all-cupcakes').empty();
        loadCupcakes();
    }
)