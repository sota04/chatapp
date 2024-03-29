# Generated by Django 4.2 on 2023-05-22 10:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Inquiry",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=40, verbose_name="お名前")),
                ("email", models.EmailField(max_length=254, verbose_name="メールアドレス")),
                ("title", models.CharField(max_length=128, verbose_name="件名")),
                ("contents", models.TextField(verbose_name="内容")),
                (
                    "posted_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="お問い合わせ日時"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Item",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="商品名")),
                ("price", models.IntegerField(verbose_name="値段")),
                ("reserve", models.IntegerField(verbose_name="予約数")),
                ("stock", models.IntegerField(verbose_name="在庫数")),
            ],
        ),
    ]
