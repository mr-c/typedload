# typedload
# Copyright (C) 2021 Salvo "LtWorf" Tomaselli
#
# typedload is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# author Salvo "LtWorf" Tomaselli <tiposchi@tiscali.it>

from time import monotonic as time
from typing import List, NamedTuple
import sys

from typedload import load
import pydantic


def timeit(f):
    r = []
    for i in range(5):
        begin = time()
        f()
        end = time()
        r.append(end - begin)
    return min(r)


class DataPy(pydantic.BaseModel):
    data: List[int]


class Data(NamedTuple):
    data: List[int]


data = {'data': list(range(3000000))}


if sys.argv[1] == '--typedload':
    print(timeit(lambda: load(data, Data)))
elif sys.argv[1] == '--pydantic':
    print(timeit(lambda: DataPy(**data)))
