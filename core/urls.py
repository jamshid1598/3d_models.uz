from django.urls import path

from .views import (
    MainView,
    Categories,
    ModelDetailView,
    PaymentView,
    FreeModelListView,
    download_counter,

    downloads,

    DiscuntView,
    
    PortfolioListView,
    PortfolioDetailView,

    VideosListView,

    AboutUsView,
    Contact,

    search_query,
)
from cart.views import (
    CartDetailView,
    add_to_cart_view,
    model_checkbox,
)


app_name='Core'

urlpatterns = [
    path('', MainView.as_view(), name = "main-view"),
    path('category/<int:pk>/', Categories.as_view(), name='category-view'),
    path('model/<slug:slug>/', ModelDetailView.as_view(), name='model-detail-view'),

    path('free/', FreeModelListView.as_view(), name='free-detail-view'),
    path('ajax/download_counter/', download_counter, name='download_counter'),

    path('ajax/downloads/', downloads, name='downloads'),

    path('payment/', PaymentView.as_view(), name='payment-view'),

    path('portfolio/', PortfolioListView.as_view(), name='portfolio-view'),
    path('portfolio/detail/<slug:slug>/', PortfolioDetailView.as_view(), name='portfolio-detail-view'),

    path('videos/', VideosListView.as_view(), name='video-view'),

    path('card/', CartDetailView.as_view(), name='card-view'),
    path('ajax/cart/detail/', add_to_cart_view, name='add_to_cart_view'),
    path('ajax/model/checkbox/', model_checkbox, name='model_checkbox'),

    path('contact/', Contact.as_view(), name='contact-view'),
    
    path('aksiya/', DiscuntView.as_view(), name='aksiya-view'),

    
    path('about/', AboutUsView.as_view(), name='about-view'),

    path('ajax/search_query/', search_query, name='search_query'),

]


# from .views import (
#     HomeView,
#     CategoryDetailView,
#     CartDetailView,
#     CheckoutDetailView,
#     CustomerProfileView,

#     # product_detail_view,
#     cart_detail_view,

#     #  Article views
#     ArticleListView,
#     article_detail_view,

#     InstallProssecc,
#     AdminControlPanel,
#     request_completed,
#     request_uncompleted,
# )

# app_name='Core'

# urlpatterns = [
    # path('', HomeView.as_view(), name='home-view'),
    
    # path('category/<int:pk>/', CategoryDetailView.as_view(), name='category-detail-view'),
    # path('category/<int:pk>/<slug:slug>/', CategoryDetailView.as_view(), name='category-detail-view'),


    # path('cart/', CartDetailView.as_view(), name='cart-detail-view'),
    # path('profile/', CustomerProfileView.as_view(), name='customer-profile-view'),
    # path('checkout/', CheckoutDetailView.as_view(), name='checkout-detail-view'),

    # # path('ajax/detail/', product_detail_view, name='product_detail_view'),
    # path('ajax/cart/detail/', cart_detail_view, name='cart_detail_view'),


    # path('article/', ArticleListView.as_view(), name='article-veiw'),
    # path('ajax/article_detail_view/', article_detail_view, name='article_detail_view'),

    # path('install-prossecc/', InstallProssecc.as_view(), name='install-veiw'),
    # path('admin-panel/', AdminControlPanel.as_view(), name='admin-veiw'),
    # path('admin-panel/<int:pk>/', AdminControlPanel.as_view(), name='admin-veiw'),
    # path('ajax/request_completed/', request_completed, name='request_completed'),
    # path('ajax/request_uncompleted/', request_uncompleted, name='request_uncompleted'),
# ]
