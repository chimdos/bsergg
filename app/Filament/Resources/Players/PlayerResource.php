<?php

namespace App\Filament\Resources\Players;

use App\Filament\Resources\Players\Pages\CreatePlayer;
use App\Filament\Resources\Players\Pages\EditPlayer;
use App\Filament\Resources\Players\Pages\ListPlayers;
use App\Models\Player;
use Filament\Forms;
use Filament\Resources\Resource;
use Filament\Tables;
use Filament\Tables\Table;
use Filament\Schemas\Schema;
use Filament\Forms\Components\Section;
use Filament\Tables\Actions\EditAction;
use Filament\Forms\Components\TextInput;
use Filament\Forms\Components\Select;

class PlayerResource extends Resource
{
    protected static ?string $model = Player::class;

    protected static string | \BackedEnum | null $navigationIcon = 'heroicon-o-user-group';

    protected static ?string $recordTitleAttribute = 'name';

   public static function form(Schema $schema): Schema
    {
        return $schema
            ->components([
                Section::make('Player Information')
                    ->schema([
                        TextInput::make('name')
                            ->required()
                            ->label("Player's Name"),
                        TextInput::make('tag')
                            ->required()
                            ->unique(ignoreRecord: true)
                            ->label('Tag (#0000)'),
                        Select::make('team_id')
                            ->relationship('team', 'name')
                            ->searchable()
                            ->preload()
                            ->label('Team')
                            ->required(),
                    ])->columns(2)
            ]);
    }

    public static function table(Table $table): Table
    {
        return $table
            ->columns([
                Tables\Columns\TextColumn::make('name')
                    ->searchable()
                    ->sortable(),
                Tables\Columns\TextColumn::make('tag')
                    ->copyable(),
                Tables\Columns\TextColumn::make('team.name')
                    ->label('Team')
                    ->badge()
                    ->color('info'),
            ])
            ->filters([
                // Futuramente podemos filtrar por região do time aqui
            ])
            ->actions([
                EditAction::make(),
            ]);
    }

    public static function getRelations(): array
    {
        return [
            //
        ];
    }

    public static function getPages(): array
    {
        return [
            'index' => ListPlayers::route('/'),
            'create' => CreatePlayer::route('/create'),
            'edit' => EditPlayer::route('/{record}/edit'),
        ];
    }
}
