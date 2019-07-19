from django.shortcuts import get_object_or_404, render

from .models import Review, Restaurant
from django.db.models import Avg
from .forms import ReviewForm
def review_list(request):
    latest_review_list = Review.objects.order_by('-pub_date')[:9]
    context = {'latest_review_list':latest_review_list}
    return render(request, 'reviews/review_list.html', context)


def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'reviews/review_detail.html', {'review': review})


def restaurant_list(request):
    restaurant_list = Restaurant.objects.order_by('-name')
    context = {'restaurant_list':restaurant_list}
    return render(request, 'reviews/restaurant_list.html', context)


def restaurant_detail(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    return render(request, 'reviews/restaurant_detail.html', {'restaurant': restaurant})

def user_review_list(request, username=None):
    if not username:
        username = request.user.username
    latest_review_list = Review.objects.filter(user_name=username).order_by('-pub_date')
    context = {'latest_review_list':latest_review_list, 'username':username}
    return render(request, 'reviews/user_review_list.html', context)

def add_review(request,restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    form = ReviewForm(request.POST)
    if form.is_valid():
        rating = form.cleaned_data['rating']
        comment = form.cleaned_data['comment']
        user_name = request.user.username
        review = Review()
        review.restaurant = restaurant
        review.user_name = user_name
        review.rating = rating
        review.comment = comment
        review.pub_date = datetime.datetime.now()
        review.save()
        #update_clusters()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('reviews:restaurant_detail', args=(restaurant.id,)))
    
    return render(request, 'reviews/restaurant_detail.html', {'restaurant': restaurant, 'form': form})
    