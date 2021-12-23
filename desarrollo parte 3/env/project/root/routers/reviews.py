from fastapi import HTTPException
from ..database import UserReview
from ..database import User
from typing import List
from ..database import Movie
from ..schemas import ReviewRequestModel
from ..schemas import reviewResponseModel
from ..schemas import ReviewRequestPutModel
from fastapi import APIRouter

router = APIRouter(prefix='/reviews')

@router.post('', response_model=reviewResponseModel)
async def create_review(user_review: ReviewRequestModel):
    if User.select().where(User.id == user_review.user_id).first() is None:
        raise HTTPException(status_code=404, detail='ey paisano que esta pasando pollo debe a ver un usuario el man no esta')
    
    if Movie.select().where(Movie.id == user_review.movie_id).first() is None:
        raise HTTPException(status_code=404, detail='esa pelicula no esta vale mia ')
    
    user_review = UserReview.create(
        user_id = user_review.user_id,
        movie_id = user_review.movie_id,
        review = user_review.review,
        score = user_review.score    
    )
    return user_review

@router.get('', response_model=List[reviewResponseModel])
async def get_reviews(page:int = 1, limit:int = 10):
    reviews = UserReview.select().paginate(page,limit)   
    return [user_review for user_review in reviews]

@router.get('/{review_id}', response_model=reviewResponseModel)
async def get_review(review_id: int):
    user_review = UserReview.select().where(UserReview.id == review_id).first()
    if user_review is None:
        raise HTTPException(status_code=404, detail='ey paisano que esta pasando vale mia no esta esa reseña que pasa')
    return user_review

@router.put('/{review_id}', response_model=reviewResponseModel)
async def update_user(review_id, review_request:ReviewRequestPutModel ):
    user_review = UserReview.select().where(UserReview.id == review_id).first()
    if user_review is None:
        raise HTTPException(status_code=404, detail='ey paisano que esta pasando vale mia no esta esa reseña que pasa')
    user_review.review = review_request.review
    user_review.score = review_request.score
    user_review.save()
    return user_review

@router.delete('/{review_id}',response_model=reviewResponseModel)
async def delete_review(review_id:int):
    user_review = UserReview.select().where(UserReview.id == review_id).first()
    if user_review is None:
        raise HTTPException(status_code=404, detail='ey paisano que esta pasando vale mia no esta esa reseña que pasa')
    user_review.delete_instance()
    return user_review