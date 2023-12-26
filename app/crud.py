from sqlalchemy.orm import Session, joinedload

from . import models, schemas


def get_movie(db: Session, movie_id: int):
    return db.query(models.Movie).options(joinedload(models.Movie.genres)).filter(models.Movie.id == movie_id).first()


def get_movie_by_name_and_year(db: Session, movie_name: str, movie_year: str):
    return db.query(models.Movie).filter(models.Movie.name == movie_name).filter(models.Movie.year == movie_year).first()


def get_movies(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Movie).offset(skip).limit(limit).all()


def create_movie(db: Session, movie: schemas.MovieCreate):
    db_movie = models.Movie(name=movie.name, year=movie.year)
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie


def get_genre(db: Session, genre_id: int):
    return db.query(models.Genre).filter(models.Genre.id == genre_id).first()


def get_genre_by_name(db: Session, genre_name: str):
    return db.query(models.Genre).filter(models.Genre.name == genre_name).first()


def get_genres(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Genre).offset(skip).limit(limit).all()


def create_genre(db: Session, genre: schemas.GenreCreate):
    db_genre = models.Genre(name=genre.name)
    db.add(db_genre)
    db.commit()
    db.refresh(db_genre)
    return db_genre


def create_movie_genre(db: Session, genre: schemas.GenreCreate, movie_id: int):
    db_genre = models.Genre(**genre.dict(), movie_id=movie_id)
    db.add(db_genre)
    db.commit()
    db.refresh(db_genre)
    return db_genre


def get_moviegenre_by_foreign_keys(db: Session, movie_id: int, genre_id: int):
    return db.query(models.MovieGenre).filter(models.MovieGenre.movie_id == movie_id).filter(models.MovieGenre.genre_id == genre_id).first()


def create_moviegenre(db: Session, moviegenre: schemas.MovieGenreCreate):
    db_moviegenre = models.MovieGenre(movie_id=moviegenre.movie_id, genre_id=moviegenre.genre_id)
    db.add(db_moviegenre)
    db.commit()
    db.refresh(db_moviegenre)
    return db_moviegenre


def get_moviegenres(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.MovieGenre).offset(skip).limit(limit).all()


def get_moviegenre(db: Session, moviegenre_id: int):
    return db.query(models.MovieGenre).filter(models.MovieGenre.id == moviegenre_id).first()