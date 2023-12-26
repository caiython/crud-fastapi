from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='Movies and Genres')

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/movie/", response_model=schemas.Movie, tags=['Movie'], status_code=status.HTTP_201_CREATED)
def create_movie(movie: schemas.MovieCreate, db: Session = Depends(get_db)):
    db_movie = crud.get_movie_by_name_and_year(db, movie_name=movie.name, movie_year=movie.year)
    if db_movie:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Movie already exists.")
    return crud.create_movie(db=db, movie=movie)


@app.get("/movie/", response_model=List[schemas.MovieAndRelationships], tags=['Movie'])
def read_movies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_movies = crud.get_movies(db, skip=skip, limit=limit)
    return db_movies


@app.get("/movie/{movie_id}", response_model=schemas.MovieAndRelationships, tags=['Movie'])
def read_movie(movie_id: int, db: Session = Depends(get_db)):
    db_movie = crud.get_movie(db, movie_id=movie_id)
    print(db_movie.__dict__)
    if db_movie is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found.")
    return db_movie


@app.put("/movie/{movie_id}", response_model=schemas.Movie, tags=['Movie'])
def update_movie(movie_id: int, movie: schemas.MovieCreate, db: Session = Depends(get_db)):
    db_movie = crud.get_movie(db, movie_id=movie_id)
    if db_movie is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found.")
    
    for key, value in movie.model_dump().items():
            setattr(db_movie, key, value)

    db.commit()
    db.refresh(db_movie)

    return db_movie


@app.delete("/movie/{movie_id}", response_model=schemas.Movie, tags=['Movie'])
def delete_movie(movie_id: int, db: Session = Depends(get_db)):
    db_movie = db.query(models.Movie).filter(models.Movie.id == movie_id).first()

    if db_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found.")
    
    db.delete(db_movie)
    db.commit()
    return db_movie
    

@app.post("/genre/", response_model=schemas.Genre, tags=['Genre'], status_code=status.HTTP_201_CREATED)
def create_genre(genre: schemas.GenreCreate, db: Session = Depends(get_db)):
    db_genre = crud.get_genre_by_name(db, genre_name=genre.name)
    if db_genre:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Genre already exists.")
    return crud.create_genre(db=db, genre=genre)


@app.get("/genre/", response_model=List[schemas.GenreAndRelationships], tags=['Genre'])
def read_genres(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_genres = crud.get_genres(db, skip=skip, limit=limit)
    return db_genres


@app.get("/genre/{genre_id}", response_model=schemas.GenreAndRelationships, tags=['Genre'])
def read_genre(genre_id: int, db: Session = Depends(get_db)):
    db_genre = crud.get_genre(db, genre_id=genre_id)
    if db_genre is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Genre not found.")
    return db_genre


@app.put("/genre/{genre_id}", response_model=schemas.Genre, tags=['Genre'])
def update_genre(genre_id: int, genre: schemas.GenreCreate, db: Session = Depends(get_db)):
    db_genre = crud.get_genre(db, genre_id=genre_id)
    if db_genre is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found.")
    
    for key, value in genre.model_dump().items():
            setattr(db_genre, key, value)

    db.commit()
    db.refresh(db_genre)

    return db_genre


@app.delete("/genres/{genre_id}", response_model=schemas.Genre, tags=['Genre'])
def delete_genre(genre_id: int, db: Session = Depends(get_db)):
    db_genre = db.query(models.Genre).filter(models.Genre.id == genre_id).first()

    if db_genre is None:
        raise HTTPException(status_code=404, detail="Movie not found.")

    db.delete(db_genre)
    db.commit()
    return db_genre


@app.post("/moviegenre/", response_model=schemas.MovieGenre, tags=['MovieGenre'], status_code=status.HTTP_201_CREATED)
def create_moviegenre(moviegenre: schemas.MovieGenreCreate, db: Session = Depends(get_db)):
    db_moviegenre = crud.get_moviegenre_by_foreign_keys(db, movie_id=moviegenre.movie_id, genre_id=moviegenre.genre_id)
    if db_moviegenre:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="MovieGenre already exists.")
    elif not crud.get_movie(db, movie_id=moviegenre.movie_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie id not found.")
    elif not crud.get_genre(db, genre_id=moviegenre.genre_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Genre id not found.")
    return crud.create_moviegenre(db=db, moviegenre=moviegenre)


@app.get("/moviegenre/", response_model=List[schemas.MovieGenre], tags=['MovieGenre'])
def read_moviegenres(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_moviegenres = crud.get_moviegenres(db, skip=skip, limit=limit)
    return db_moviegenres


@app.get("/moviegenre/{moviegenre_id}", response_model=schemas.MovieGenre, tags=['MovieGenre'])
def read_moviegenre(moviegenre_id: int, db: Session = Depends(get_db)):
    db_moviegenre = crud.get_moviegenre(db, moviegenre_id=moviegenre_id)
    if db_moviegenre is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Genre not found.")
    return db_moviegenre


@app.put("/moviegenre/{moviegenre_id}", response_model=schemas.MovieGenre, tags=['MovieGenre'])
def update_moviegenre(moviegenre_id: int, moviegenre: schemas.MovieGenreCreate, db: Session = Depends(get_db)):
    db_moviegenre = crud.get_moviegenre(db, moviegenre_id=moviegenre_id)
    if db_moviegenre is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="MovieGenre not found.")
    elif not crud.get_movie(db, movie_id=moviegenre.movie_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie id not found.")
    elif not crud.get_genre(db, genre_id=moviegenre.genre_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Genre id not found.")

    for key, value in moviegenre.model_dump().items():
            setattr(db_moviegenre, key, value)

    db.commit()
    db.refresh(db_moviegenre)

    return db_moviegenre


@app.delete("/moviegenre/{moviegenre_id}", response_model=schemas.MovieGenre, tags=['MovieGenre'])
def delete_moviegenre(moviegenre_id: int, db: Session = Depends(get_db)):
    db_moviegenre = db.query(models.MovieGenre).filter(models.Genre.id == moviegenre_id).first()

    if db_moviegenre is None:
        raise HTTPException(status_code=404, detail="MovieGenre not found.")

    db.delete(db_moviegenre)
    db.commit()
    return db_moviegenre

