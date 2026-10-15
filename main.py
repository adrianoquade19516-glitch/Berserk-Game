"""Ponto de entrada do jogo Berserk."""
from database.connection import get_connection, init_db
from ui import menus


def main():
    conn = get_connection()
    try:
        init_db(conn)
        menus.run(conn)
    except (KeyboardInterrupt, EOFError):
        print("\nJogo terminado.")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
