import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))
from renderer import Renderer
from difficulty import Difficulty
from minefield import Minefield


class TestRenderer:
    def hard_field_renderer():
        field = Minefield(Difficulty.HARD.value[0], Difficulty.HARD.value[2])
        return Renderer(field)

    def easy_field_renderer():
        field = Minefield(Difficulty.EASY.value[0], Difficulty.EASY.value[2])
        return Renderer(field)

    def medium_field_renderer():
        field = Minefield(Difficulty.MEDIUM.value[0], Difficulty.MEDIUM.value[2])
        return Renderer(field)

    @pytest.mark.parametrize('renderer, expected_width, expected_height', [
        (easy_field_renderer(), 160, 260),
        (medium_field_renderer(), 256, 356),
        (hard_field_renderer(), 352, 452)
    ])
    def test_field_size(self, renderer, expected_width, expected_height):
        assert renderer.window_width == expected_width
        assert renderer.window_height == expected_height

    @pytest.mark.parametrize('renderer, expected', [
        (easy_field_renderer(), (69, 10, 23, 23)),
        (medium_field_renderer(), (117, 10, 23, 23)),
        (hard_field_renderer(), (165, 10, 23, 23))
    ])
    def test_get_menu_button_coords(self, renderer, expected):
        assert renderer.get_menu_button_coords() == expected

    @pytest.mark.parametrize('renderer, expected', [
        (easy_field_renderer(), (0, 100, 160, 160)),
        (medium_field_renderer(), (0, 100, 256, 256)),
        (hard_field_renderer(), (0, 100, 352, 352))
    ])
    def test_get_field_coords(self, renderer, expected):
        assert renderer.get_field_coords() == expected

    @pytest.mark.parametrize('renderer, expected', [
        (easy_field_renderer(), (88, 49, 56, 56)),
        (medium_field_renderer(), (152, 81, 56, 56)),
        (hard_field_renderer(), (216, 113, 56, 56))
    ])
    def test_get_restart_button_coords(self, renderer, expected):
        assert renderer.get_restart_button_coords() == expected

    @pytest.mark.parametrize('renderer, expected', [
        (easy_field_renderer(), (16, 49, 56, 56)),
        (medium_field_renderer(), (48, 81, 56, 56)),
        (hard_field_renderer(), (80, 113, 56, 56))])
    def test_get_resume_button_coords(self, renderer, expected):
        assert renderer.get_resume_button_coords() == expected

    @pytest.mark.parametrize('renderer, expected', [
        (easy_field_renderer(), (88, 155, 56, 56)),
        (medium_field_renderer(), (152, 219, 56, 56)),
        (hard_field_renderer(), (216, 283, 56, 56))
    ])
    def test_get_exit_button_coords(self, renderer, expected):
        assert renderer.get_exit_button_coords() == expected

    @pytest.mark.parametrize('renderer, expected', [
        (easy_field_renderer(), (16, 155, 56, 56)),
        (medium_field_renderer(), (48, 219, 56, 56)),
        (hard_field_renderer(), (80, 283, 56, 56))
    ])
    def test_get_stats_button_coords(self, renderer, expected):
        assert renderer.get_stats_button_coords() == expected

    @pytest.mark.parametrize('renderer, expected', [
        (easy_field_renderer(), (66, 222, 28, 28)),
        (medium_field_renderer(), (114, 318, 28, 28)),
        (hard_field_renderer(), (162, 414, 28, 28))
    ])
    def test_get_back_button_coords(self, renderer, expected):
        assert renderer.get_back_button_coords() == expected
