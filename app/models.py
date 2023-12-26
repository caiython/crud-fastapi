from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .database import Base


class MovieGenre(Base):
    __tablename__ = "movie_genre"

    id: Mapped[int] = mapped_column(primary_key=True)
    movie_id: Mapped[int] = mapped_column(ForeignKey("movie.id"))
    genre_id: Mapped[int] = mapped_column(ForeignKey("genre.id"))

    movie: Mapped["Movie"] = relationship(back_populates="genre_associations")
    genre: Mapped["Genre"] = relationship(back_populates="movie_associations")


class Movie(Base):
    __tablename__ = "movie"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    year: Mapped[str] = mapped_column(nullable=True)
    
    genres: Mapped[List["Genre"]] = relationship(secondary="movie_genre", back_populates="movies", overlaps='genre,movie')
    genre_associations: Mapped[List["MovieGenre"]] = relationship(back_populates="movie", overlaps='genres,movies')


class Genre(Base):
    __tablename__ = "genre"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()

    movies: Mapped[List["Movie"]] = relationship(secondary="movie_genre", back_populates="genres", overlaps='movie,genre')
    movie_associations: Mapped[List["MovieGenre"]] = relationship(back_populates="genre", overlaps='movies,genres')

