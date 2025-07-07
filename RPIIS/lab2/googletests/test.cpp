#pragma warning(disable : 26495)
#include "pch.h"
#include <gtest/gtest.h>
#include "../lab 2/set_parser.h"
#include "../lab 2/set_element.h"
#include "../lab 2/cartesian_product.h"


// Тесты парсинга
TEST(ParseSetTest, BasicTest) {
    std::string input = "1, 2, {a, b}";
    std::vector<SetElement> expected = {
        SetElement("1"),
        SetElement("2"),
        SetElement({SetElement("a"), SetElement("b")})
    };
    std::vector<SetElement> result = parseSet(input);

    ASSERT_EQ(expected.size(), result.size());
    for (size_t i = 0; i < expected.size(); ++i) {
        EXPECT_EQ(expected[i].isAtomic, result[i].isAtomic);
        if (expected[i].isAtomic) {
            EXPECT_EQ(expected[i].value, result[i].value);
        }
        else {
            ASSERT_EQ(expected[i].subset.size(), result[i].subset.size());
            for (size_t j = 0; j < expected[i].subset.size(); ++j) {
                EXPECT_EQ(expected[i].subset[j].value, result[i].subset[j].value);
            }
        }
    }
}

TEST(ParseSetTest, EmptyInputTest) {
    std::string input = "";
    std::vector<SetElement> expected = {};
    std::vector<SetElement> result = parseSet(input);

    ASSERT_EQ(expected.size(), result.size());
}

TEST(ParseSetTest, NestedSubsetsTest) {
    std::string input = "1, {2, {3, 4}}, {a, b}";
    std::vector<SetElement> expected = {
        SetElement("1"),
        SetElement({SetElement("2"), SetElement({SetElement("3"), SetElement("4")})}),
        SetElement({SetElement("a"), SetElement("b")})
    };
    std::vector<SetElement> result = parseSet(input);

    ASSERT_EQ(expected.size(), result.size());
    for (size_t i = 0; i < expected.size(); ++i) {
        EXPECT_EQ(expected[i].isAtomic, result[i].isAtomic);
        if (expected[i].isAtomic) {
            EXPECT_EQ(expected[i].value, result[i].value);
        }
        else {
            ASSERT_EQ(expected[i].subset.size(), result[i].subset.size());
            for (size_t j = 0; j < expected[i].subset.size(); ++j) {
                EXPECT_EQ(expected[i].subset[j].isAtomic, result[i].subset[j].isAtomic);
                if (expected[i].subset[j].isAtomic) {
                    EXPECT_EQ(expected[i].subset[j].value, result[i].subset[j].value);
                }
                else {
                    ASSERT_EQ(expected[i].subset[j].subset.size(), result[i].subset[j].subset.size());
                    for (size_t k = 0; k < expected[i].subset[j].subset.size(); ++k) {
                        EXPECT_EQ(expected[i].subset[j].subset[k].value, result[i].subset[j].subset[k].value);
                    }
                }
            }
        }
    }
}

TEST(ParseSetTest, SingleElementTest) {
    std::string input = "x";
    std::vector<SetElement> expected = { SetElement("x") };
    std::vector<SetElement> result = parseSet(input);

    ASSERT_EQ(expected.size(), result.size());
    EXPECT_EQ(expected[0].isAtomic, result[0].isAtomic);
    EXPECT_EQ(expected[0].value, result[0].value);
}

TEST(ParseSetTest, InvalidInputTest) {
    std::string input = "1, {, 2"; // Некорректный ввод с незакрытой скобкой
    std::vector<SetElement> result = parseSet(input);
    ASSERT_TRUE(result.empty()); // Ожидаем, что функция вернёт пустой вектор для некорректного ввода
}

// Тесты Декартова произведения
TEST(CartesianProductTest, TwoSets) {
    std::vector<std::vector<SetElement>> sets = {
        {SetElement("1"), SetElement("2")},
        {SetElement("a"), SetElement("b")}
    };
    std::vector<std::vector<SetElement>> expected = {
        {SetElement("1"), SetElement("a")},
        {SetElement("1"), SetElement("b")},
        {SetElement("2"), SetElement("a")},
        {SetElement("2"), SetElement("b")}
    };
    auto result = cartesianProduct(sets);

    ASSERT_EQ(expected.size(), result.size());
    for (size_t i = 0; i < expected.size(); ++i) {
        ASSERT_EQ(expected[i].size(), result[i].size());
        for (size_t j = 0; j < expected[i].size(); ++j) {
            EXPECT_EQ(expected[i][j].value, result[i][j].value);
        }
    }
}

TEST(CartesianProductTest, EmptySetTest) {
    std::vector<std::vector<SetElement>> sets = {
        {},
        {SetElement("a"), SetElement("b")}
    };
    std::vector<std::vector<SetElement>> expected = {};
    auto result = cartesianProduct(sets);

    ASSERT_EQ(expected.size(), result.size());
}

TEST(CartesianProductTest, ThreeSetsTest) {
    std::vector<std::vector<SetElement>> sets = {
        {SetElement("1"), SetElement("2")},
        {SetElement("a"), SetElement("b")},
        {SetElement("x"), SetElement("y")}
    };
    std::vector<std::vector<SetElement>> expected = {
        {SetElement("1"), SetElement("a"), SetElement("x")},
        {SetElement("1"), SetElement("a"), SetElement("y")},
        {SetElement("1"), SetElement("b"), SetElement("x")},
        {SetElement("1"), SetElement("b"), SetElement("y")},
        {SetElement("2"), SetElement("a"), SetElement("x")},
        {SetElement("2"), SetElement("a"), SetElement("y")},
        {SetElement("2"), SetElement("b"), SetElement("x")},
        {SetElement("2"), SetElement("b"), SetElement("y")}
    };
    auto result = cartesianProduct(sets);

    ASSERT_EQ(expected.size(), result.size());
    for (size_t i = 0; i < expected.size(); ++i) {
        ASSERT_EQ(expected[i].size(), result[i].size());
        for (size_t j = 0; j < expected[i].size(); ++j) {
            EXPECT_EQ(expected[i][j].value, result[i][j].value);
        }
    }
}

TEST(CartesianProductTest, SingleElementSetsTest) {
    std::vector<std::vector<SetElement>> sets = {
        {SetElement("1")},
        {SetElement("a")}
    };
    std::vector<std::vector<SetElement>> expected = {
        {SetElement("1"), SetElement("a")}
    };
    auto result = cartesianProduct(sets);

    ASSERT_EQ(expected.size(), result.size());
    for (size_t i = 0; i < expected.size(); ++i) {
        ASSERT_EQ(expected[i].size(), result[i].size());
        for (size_t j = 0; j < expected[i].size(); ++j) {
            EXPECT_EQ(expected[i][j].value, result[i][j].value);
        }
    }
}

TEST(CartesianProductTest, InvalidInputTest) {
    std::vector<std::vector<SetElement>> sets = {};
    std::vector<std::vector<SetElement>> expected = {};
    auto result = cartesianProduct(sets);

    ASSERT_EQ(expected.size(), result.size());}