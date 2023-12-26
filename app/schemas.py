from typing import Union, List, ForwardRef

from pydantic import BaseModel


class MovieBase(BaseModel):
    name: str
    year: Union[str, None] = None


class MovieCreate(MovieBase):
    pass


class Movie(MovieBase):
    id: int

    class Config:
        from_attributes = True


class GenreBase(BaseModel):
    name: str


class GenreCreate(GenreBase):
    pass


class Genre(GenreBase):
    id: int

    class Config:
        from_attributes = True


class MovieGenreBase(BaseModel):
    movie_id: int
    genre_id: int


class MovieGenreCreate(MovieGenreBase):
    pass


class MovieGenre(MovieGenreBase):
    id: int

    class Config:
        from_attributes = True


class MovieAndRelationships(Movie):
    genres: List[GenreBase]


class GenreAndRelationships(Genre):
    movies: List[MovieBase]

